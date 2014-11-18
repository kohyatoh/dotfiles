set_ps1() {
    local g='\[\e[1;32m\]'
    local b='\[\e[1;34m\]'
    local n='\[\e[0m\]'
    PS1="$g\t$n $b\w$n $b\$$n "
}
set_ps1
HISTTIMEFORMAT='%y/%m/%d %H:%M:%S '
