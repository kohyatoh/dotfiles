#!/usr/bin/env python
import glob, os, shutil, sys
import xml.etree.ElementTree as ET

NS = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace('', NS)
ASSEMBLY_PLUGIN_CONFIG = """<plugin>
  <artifactId>maven-assembly-plugin</artifactId>
  <configuration>
    <descriptorRefs>
      <descriptorRef>jar-with-dependencies</descriptorRef>
    </descriptorRefs>
  </configuration>
</plugin>"""

def get_or_create(elem, tag):
    c = elem.find(tag)
    if c is None:
        c = ET.Element(tag)
        elem.append(c)
    return c

def pom_with_deps(filename):
    xml = ET.parse(filename)
    project = xml.getroot()
    build = get_or_create(project, "{%s}build" % NS)
    plugins = get_or_create(build, "{%s}plugins" % NS)
    plugins.append(ET.XML(ASSEMBLY_PLUGIN_CONFIG))
    return ET.tostring(project)

def main(argv):
    pom = argv[1] if len(argv) > 1 else "pom.xml"
    tmpdir = "tmp"
    target = "deps.jar"
    cmd = "mvn assembly:single"
    print "Creating temporary maven project under %s..." % tmpdir
    os.mkdir(tmpdir)
    try:
        with open(tmpdir + "/pom.xml", "w") as f:
            print >>f, pom_with_deps(pom)
        print "Creating jar..."
        print "> " + cmd
        os.system("cd %s; %s" % (tmpdir, cmd))
        jar = glob.glob(tmpdir + "/target/*-with-dependencies.jar")[0]
        print "Copying jar to %s..." % target
        shutil.copyfile(jar, target)
    finally:
        shutil.rmtree(tmpdir)

if __name__ == "__main__":
    main(sys.argv)
