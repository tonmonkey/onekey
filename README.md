# onekey
爱*查批量查询目标公司所有控股子公司、投资子公司。采用多层遍历递归查询，覆盖面全包括

## Good point
+ 递归遍历收集更加准确无遗漏
+ 一键完成前期暴露面资产收集
+ 持续维护

## How to use
1. 配置文件填入Cookie与目标公司Pid值
2. 运行：python3 main.py -h
3. 程序有两种运行模式：1.常规模式，2.递归模式。常规模式适用与查询公司旗下子公司和投资公司，深度为1层。递归模式适用与深度挖掘公司旗下所有控股子公司(50%以上)，查询深度无限。
4. 运行结束会在当前目录输出excel结果
  
## Next plan
  + <del>添加递归查询模块</del>
  + <del>结果输出中输出更多字段<del>
  + 采用多线程
  + 添加fofa API接口模块，数据收集平稳衔接
  + 添加端口扫描模块
  + 添加指纹识别模块

## Show
Get PID:
![image](https://github.com/tonmonkey/onekey/assets/84943423/338ca3a9-62df-4e63-8b76-bc933be479ad)
Setting:
根据需要选择配置代理，pid,inpid,cookie
![image](https://github.com/tonmonkey/onekey/assets/84943423/02a8823f-fbe4-44e1-96a1-3631b865c61f)
Running:
![q1](https://github.com/tonmonkey/onekey/assets/84943423/6e4f8b93-87e0-4a2b-8bdf-c0917b173f45)

