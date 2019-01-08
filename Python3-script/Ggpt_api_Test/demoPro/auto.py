#coding = utf-8
import yaml

# tmp = None
with open("boss_api.yml", "r") as f:
    tmp = yaml.load(f)



for key, value in tmp.items():
    str_tmp = """suiteName: %s 
testCase:
  - case 1:
      testCaseName: 参数正确,
      tag: smoke""" % key
    try:
        data = value["json"]

        str_tmp += """
      json:"""
        for k in data.keys():
            str_tmp += """
        %s: """ % k
    except KeyError:
        if "formData" in value.keys():
            data = value["formData"]
            str_tmp += """
      formData: """
            for k in data.keys():
                str_tmp += """
        %s: """ % k
        elif "params" in value.keys():
            data = value["params"]
            str_tmp += """
      params: """
            for k in data.keys():
                str_tmp += """
        %s: """ % k

    str_tmp += """  
      validate:
        - eq: ["status_code", 200]
        - eq: ["%s.code", 0]"""%key.split(".")[0]
    file = key+".yml"
    with open("./case/"+file, "w") as f:
        f.write(str_tmp)