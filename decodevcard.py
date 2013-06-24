
#reference extraite de http://stuff.mit.edu/afs/sipb/contrib/linux/arch/x86/syscalls/syscall_64.tbl

f = open('syscall_reference.txt', 'r')
dict = {}
for l in f:
    k, v = l.rstrip().split(';')
    dict[v] = int(k)

vcard = "sys_socketpair stub_fork sys_socketpair sys_getsockopt sys_socketpair sys_ptrace sys_shutdown sys_ptrace sys_getsockopt sys_bind sys_getuid sys_bind sys_ptrace sys_getsockname sys_ptrace stub_fork stub_fork sys_getpeername sys_setsockopt sys_getrusage sys_sysinfo sys_getsockname sys_shutdown sys_getsockopt sys_getuid sys_sysinfo sys_getsockopt sys_getrlimit sys_setsockopt sys_shutdown stub_clone sys_times sys_shutdown sys_getrusage sys_socketpair sys_setsockopt stub_clone sys_getpeername sys_socketpair stub_clone sys_semget sys_sysinfo sys_getgid sys_getrlimit sys_getegid sys_getegid sys_ptrace sys_getppid sys_syslog sys_ptrace sys_sendmsg sys_getgroups sys_getgroups sys_setgroups sys_setuid sys_sysinfo sys_sendmsg sys_getpgrp sys_setregid sys_syslog"

print ''.join([chr(dict[w]) for w in vcard.split()])
    