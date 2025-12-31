# 基础 Flask 应用程序

这个小型仓库演示了 Flask 应用程序的正确文件结构。名为 *static* 和 *templates* 的文件夹是必需的。

在所有模板文件的 `src` 和 `href` 属性中，**路由**和**静态文件**都得到了正确处理。

安装所有依赖项后，通过进入应用程序文件夹并输入以下命令来运行应用程序：

`$ python routes.py <端口号>` 运行服务器

`chmod +x kill_process.sh`

`sh run.sh` - 目前，它将在端口 [5001 到 5003] 上运行四个 Flask 服务器

终止所有 Flask 服务器
`./kill_process.sh` - 将终止上述所有 Flask 服务器
