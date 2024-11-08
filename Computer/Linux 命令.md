## 1. 文件与目录操作

ls：列出当前目录中的文件
ls -l：以详细信息格式列出文件
ls -a：显示所有文件，包括隐藏文件（以.开头）

cd directory：进入指定目录
cd ~：返回用户主目录
cd ..：返回上一级目录

pwd：输出当前所在目录的绝对路径

xdg-open file_or_dir：使用默认的桌面应用程序打开文件/目录

cp source destination：复制文件
cp -r source_dir dest_dir：递归复制目录

mv oldname newname：重命名文件
mv file directory：移动文件

touch file：创建一个空文件或更新已有文件的修改时间
mkdir new_dir：创建一个新目录
mkdir -p directory：递归创建多层目录

rm file：删除文件
rm -f file：强制删除文件（无提示）
rm -r directory：递归删除目录及其内容
rmdir directory：仅删除空目录

## 2. 文件内容查看

cat file：从头到尾显示文件内容
more file：逐页查看文件内容
less file：使用上下键翻页查看文件

head file：显示文件前 10 行
head -n 20 file：显示文件前 20 行

tail file：显示文件后 10 行
tail -n 20 file：显示文件最后 20 行
tail -f file：动态查看文件末尾（如日志文件）

## 3. 文件权限与所有权

chmod 755 file：给文件设置读/写/执行权限 (755)
chmod u+x file：给文件拥有者增加执行权限

chown user file：更改文件所有者为指定用户
chown user:group file：更改文件的用户和组

## 4. 压缩与解压

tar -cvf archive.tar file_or_dir：打包文件/目录为 .tar 文件
tar -xvf archive.tar：解压 .tar 文件
tar -czvf archive.tar.gz file_or_dir：压缩为 .tar.gz 格式
tar -xzvf archive.tar.gz：解压 .tar.gz 文件

zip archive.zip file_or_dir：压缩为 zip 文件
unzip archive.zip：解压 zip 文件

## 5. 系统管理

sudo command：以超级用户身份执行命令

df -h：以可读格式查看磁盘使用情况
free -h：以可读格式查看内存使用情况
du -h file_or_dir：查看指定文件或目录的大小
du -sh directory：显示目录总大小

top：显示实时的系统资源使用情况
ps：列出当前会话的进程
ps aux：列出所有进程
kill process_id：根据进程 ID 终止进程
kill -9 process_id：强制终止进程

uptime：显示系统运行时间、用户数量和系统负载

## 6. 网络操作

ping google.com：检查与指定域的网络连接

ifconfig：查看网络接口配置信息
ip addr：查看网络接口的 IP 地址信息
ip link show：显示网络接口的状态

wget http://example.com/file：从指定URL下载文件
curl http://example.com：获取网页内容

## 7. apt

### 7.1. apt-cache

apt list --installed：列出所有已安装的软件包

apt list <package_name>：检查指定软件包是否已安装，以及其状态
apt-cache show <package_name>：显示关于某个软件包的详细信息
apt-cache search <package_name>：在包列表中查找包含指定关键词的软件包
　i：installed（该软件包已经被安装并可使用）
　p：purged（该软件包已被彻底删除，包括所有文件和配置文件）
　r：removed（该软件包已经被删除，但保留了其配置文件）
　c：config-files（该软件包的可执行文件已经被删除，但保留了它的配置文件）
　v：virtual package（该软件包是虚拟包，没有实际的文件，只是为了满足依赖关系的占位符）
　h：half-installed（该软件包处于安装或卸载未完成的状态）
　u：unpacked（该软件包的文件已经被解压，但尚未配置）
　b：broken（该软件包处于损坏状态，可能依赖项未被满足或其他问题）

### 7.2. apt-get

apt-get update：更新软件包可用版本列表

apt list --upgradable：列出所有有可用更新的软件包
apt-get upgrade：升级已安装的软件包（不会移除任何现有的软件包）

apt-get install <package_name>：安装新软件包
apt-get reinstall <package_name>：重新安装软件包
apt-get --fix-broken install：修复损坏的依赖关系，并安装缺失的依赖包
apt-get download <package_name>：下载指定的软件包文件（.deb）到当前目录（不安装）
apt-get source <package_name>：下载源码包文件

apt-get remove <package_name>：删除软件包的可执行文件和库文件（保留配置文件）
apt-get purge <package_name>：删除软件包的所有文件（包括配置文件）
apt-get autoremove：删除无用的包和依赖项
apt-get clean：删除下载的软件包缓存（.deb 文件）

### 7.3. apt-mark

apt-mark hold <package_name>：标记软件包为保留(held back)
apt-mark unhold <package_name>：取消软件包的保留(held back)标记
apt-mark showhold ：列出设为保留的软件包

apt-mark auto <package_name>：标记软件包为自动安装
apt-mark showauto ：列出所有自动安装的软件包

apt-mark manual <package_name>：标记软件包为手动安装
apt-mark showmanual ：列出所有手动安装的软件包

apt-mark minimize-manual：标记所有元软件包的依赖为自动安装
