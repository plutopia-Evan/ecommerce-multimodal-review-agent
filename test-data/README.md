# 测试数据说明

本目录中的图片和文本仅用于工作流功能测试，不包含真实用户信息。

| 文件 | 用途 | 预期图片结论 |
|---|---|---|
| `images/normal-product.png` | 正常保温杯商品图 | `image_ok` |
| `images/blurred-product.png` | 模糊但无恶意内容 | `image_low_quality` |
| `images/unrelated-content.png` | 与商品无关的内容 | `image_low_quality` |
| `images/advertising-diversion.png` | 含虚构联系方式和伪二维码 | `malicious` |

广告图中的联系方式为测试占位符，二维码不用于真实导流。
