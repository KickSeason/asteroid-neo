#!/usr/bin/expect

set timeout -1

cd neo-cli

spawn dotnet neo-cli.dll --no-peers /rpc

expect "neo>"

expect eof
