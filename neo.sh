#!/usr/bin/expect

set timeout -1


set checkpoint [lindex $argv 0];

cd neo-cli

spawn dotnet neo-cli.dll --no-peers /rpc

expect "neo>"

if {[lindex $argv 0] == "1"} {
    sleep 3600
    send "exit\r"
}

expect eof
