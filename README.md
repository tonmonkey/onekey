# onekey
通过爱企查批量导出总公司旗下所有控股子公司

## how to use
python3 main.py -h  
usage: QAQC.py [-h] [-i ID]  
options:  
  -h, --help      show this help message and exit  
  -i ID, --id ID  Input you wang query company ID
  
## Next plan
  + 添加公司名称查询方式
  + 结果导出展示更多信息:icp备案，邮箱，电话等
  + 引入子域名查询(oneforall,fofa),爆破功能
  + 增加端口扫描(namp,masscan)功能(可自定义扫描端口)
  + 增加poc模块(xray,nuclei)与爬虫(rad)
