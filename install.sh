cd /var/www/asteroid-neo

apt-get update

apt-get -y install unzip \
    curl \
    apt-transport-https \
    wget \
    expect \
    libunwind8 \
    icu-devtools \
    libleveldb-dev \
    sqlite3 \
    libsqlite3-dev \
    libunwind8-dev \
    supervisor

## dotnet
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list'

apt-get update
apt-get -y install dotnet-sdk-2.1.104

rm -rf /var/lib/apt/lists/*


## neo-cli
wget "https://github.com/neo-project/neo-cli/releases/download/v2.7.4/neo-cli-linux-x64.zip"
unzip neo-cli-linux-x64.zip
rm neo-cli-linux-x64.zip
