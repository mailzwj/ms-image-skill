# 图像生成技能
(ms-image-skill)，Qwen-Image-2512

## 安装

```bash
cd .claude/skills # 进入技能安装目录
git clone https://github.com/mailzwj/ms-image-skill.git #下载技能源码
cd ms-image-skill # 进入技能目录
pip install -r requirements.txt # 安装依赖
```

## 配置

### 手动配置
1. 获取[模型服务访问令牌](https://modelscope.cn/my/access/token)
2. 编辑`config.json`文件，填入模型服务访问令牌
```json
// ms-image-skill/config.json
{
    "api_key": "your modelscope token"
}
```

### 自动配置
启动`Claude code`，输入`/ms-image-skill 添加配置`，按照提示输入模型服务访问令牌，运行即可。配置文件保存在本地，安全可靠。

## 示例

```bash
# Step 1: 进入项目空间
cd workspace

# Step 2: 启动Claude code
claude

# Step 3: 输入以下指令
/ms-image-skill 生成一张图片 # 或者直接输入“生成一张图片”，Claude会自动识别skill
# Step 3.1: 参数+提示词
640x960, 电影光效，一个年轻的中国姑娘，长发，皮肤白皙，手上拿着一本翻开的书，站在书架中间，认真的阅读
# Step 4: 等待生成结果

# Step 5: 查看生成结果
ls ms_img_outputs
```
