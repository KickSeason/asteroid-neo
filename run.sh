set timeout -1

cd /var/www/asteroid-neo/neo-cli

spawn dotnet neo-cli.dll --no-peers /rpc

expect "neo>"

expect eof
