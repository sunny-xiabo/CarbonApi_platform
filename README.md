**该接口自动化测试框架使用Pytest单元测试框架+requests接口请求模块+yaml数据配置+csv数据驱动+allure测试报告框架进行封装**

使用该测试框架做接口自动化测试时:

    1、首先按照格式编该接口对应的yaml配置文件
    2、然后按照格式编写改接口的csv数据文件
    3、编写该接口的测试用例
    4、在测试用例中获取所有请求数据进行参数化
    5、然后调用请求工具类进行接口请求
    6、同时把相关数据输出到日志和allure附加内容中，使测试报告更加直观
    7、测试报告将记录该接口执行的相关请求数据、响应数据以及断言数据
    


**config**
`配置文件`

        config： 文件目录配置文件
        scene: 场景yml文件夹

        #yml只是每个接口所需的配置文件,具体数据需要去csv中读取,yml文件名与csv数据文件名保持一致
        #内部用到所有的参数键名称与接口相关参数名保持一致
        #其中没有的值使用~表示None
        # csv中第一行数据写与参数名保持一致的名称,第二行写接口验证通过性的数据
        #csv中不写依赖的字段及字段值

        单接口yml模板：
            name: *
            method: *
            url: *
            headers: ~
            params: ~
            data: ~
            json: ~
            validate:
             statusCode: ~
             errorCode: ~
             msg: ~

        场景接口（多接口）yml模板
            - name: *
              method: *
              url: *
              headers: ~
              params: ~
              data: ~
              json: ~
              validate:
               statusCode: ~
               errorCode: ~
               msg: ~
              extract:
                body: ~
                headers: ~
              depend: ~
                headers: ~
                params: ~
                data: ~
                json: ~



**data**
`数据文件`

**json**
`allure报告所需json数据`

**logs**
`记录运行日志`

**reports**
`allure报告`

**run**
`pytest运行`

        1、执行main函数，进行pytest单元测试
        2、执行allure，生成报告
            allure generate ./json -o ./reports --clean
        3、启动allure服务
            allure open reports --host 127.0.0.1 --port 8800
            输入地址 查看报告

        -s: 显示程序中的print / logging 输出
        -V：丰富信息模式，输出更详细的用例执行信息
        -q: 安静模式，不输出环境信息
        -k: 关键字匹配，用and区分：匹配范围（文件名、类名、函数名）

**test_cases**
`测试用例`

**utils**
`工具类`

        log: log日志工具类
        CsvUtil: csv工具类
        requestDataUtil: 获取请求数据工具类
        requestUtil: 发送网络请求工具类
        YamlUtil: 读取yml配置文件工具类
        SceneRquestUtil: 场景工具类

    


