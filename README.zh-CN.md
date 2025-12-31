# 基础 Flask 应用

这个小仓库展示了一个 Flask 应用的正确文件结构。名为 *static* 和 *templates* 的文件夹是必需的。

**路由** 和 **静态文件** 在模板文件中的所有 `src` 和 `href` 属性中都得到了正确处理。

安装所有依赖后，进入其文件夹并输入以下命令运行应用程序：

`$ python routes.py <端口号>` 运行服务器

`chmod +x kill_process.sh`

`sh run.sh` - 目前，它将在端口 [5001 到 5003] 上运行四个 Flask 服务器

要杀死所有 Flask 服务器
`./kill_process.sh` - 将杀死上述所有 Flask 服务器