# coding = utf-8
from Lib.write_Log import MyLog
from Lib import draw_chart
import time
import traceback


class WriteReport:
    def __init__(self):
        self.rowid = 0
        self.result_html = ''
        self.if_html = ''
        self.pass_num = 0
        self.fail_num = 0
        self.un_num = 0
        self.prj_name = ''
        self.if_name = ''
        self.if_total = 0
        self.total_time = 0
        self.if_pass, self.if_fail, self.if_error, self.if_time = 0, 0, 0, 0
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.report_path = self.log.get_log_path()

    def set_prj_name(self, prj_name):
        self.prj_name = prj_name

    def set_if_total(self):
        self.if_total += 1

    def set_pass_num(self):
        self.pass_num += 1

    def set_fail_num(self):
        self.fail_num += 1

    def set_un_num(self):
        self.un_num += 1

    def set_if_info(self):
        info_html = self.if_info_html(self.if_name, self.if_time,
                                      [self.if_total, self.if_pass, self.if_fail, self.if_error])
        self.if_html += info_html + self.result_html
        self.total_time += self.if_time
        self.if_pass, self.if_fail, self.if_error, self.if_time = 0, 0, 0, 0
        self.result_html = ''

    def state_html(self, case_name, run_time, result, msg, response, param):

        response = response.strip('\n')
        color = 'black'
        b_color = "white"
        self.if_time += run_time
        self.if_name,case_name = case_name.split(":", 1)
        if result == 0:
            result = 'Pass'
            self.if_pass += 1
        elif result in range(10,20):
            result = "Error"
            color = 'orangered'
            b_color = "seashell"
            self.if_error += 1
        else:
            result = 'Failed'
            color = 'orchid'
            b_color = "seashell"
            self.if_fail += 1
        # if self.prj_name == '':
        #     self.prj_name = case_name.split('/')[0]
        if_id = "if"+str(self.if_total+1)+"-"+str(self.if_pass+self.if_fail+self.if_error)
        rowid = if_id.replace("if", "row")
        # if not (self.if_pass+self.if_fail+self.if_error) % 2:
        #     b_color = "seashell"
        # else:
        #     b_color = "white"
        st_html = """
<tr id="%s" align="center" style="background-color:%s;display:none;word-break:break-all">
    <th align="left">__%s</th>
    <th>%.7f</th>
    <th style='color:%s' >%s</th>
    <th align="left">%s</th>
    <th><input id="intest" value="Show Detail" type='button' style='color:black' onclick="setDetailMsgRow(%s,this)"></th>
</tr>""" % (if_id, b_color, case_name, run_time, color, result, msg, [rowid, rowid + '-1'])

        param_html = """
        <tr id="%s" style="display:none;color:%s;word-break:break-all" >
        <th align="left" colspan='1' style="font-size:14">
        Params 
        </th>
        <th align="left" colspan='4' >
        %s
        </th>
        </tr>""" % (rowid+'-1', color, param)

        re_html = """
        <tr id="%s" style="display:none;color:%s;word-break:break-all" >
        <th align="left" colspan='1' style="font-size:14">
        Response Data
        </th>
        <th align="left" colspan='4' >
        %s
        </th>
        </tr>""" % (rowid, color, response)
        self.result_html += st_html + param_html + re_html
        self.rowid += 1

    @staticmethod
    def if_info_html(if_name, r_time, result):
        if not result[0]%2:
            style = "background-color:seashell"
        else:
            style = "background-color:white"

        if_html = """
        <tr align="center" style=%s>
        <th  align="left" colspan="1" style="font-size: 15">
        测试套件名称：%s 
        </th>
         <th colspan="1" style="font-size: 15">%.6f</th> 
        <th  align="left" colspan="2" style="font-size: 15">
            用例共计：%s,  通过：%s, 失败：%s, 错误：%s
        </th>
        <th align="center" colspan="1">
         <input id="intest" value="查看详情" type='button' style='color:black' onclick="showRow([%s,%s],this)">
        </th>
        </tr>
        """ % (style, if_name, r_time, result[1] + result[2] + result[3], result[1],
               result[2], result[3], result[0], result[1] + result[2] + result[3])
        return if_html

    def report(self):
        html = """       
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>InterfaceTesting</title>
<style type="text/css">
            div#global{
                width: 100%%;
                height: 800px;
                background-color: silver; 
            }
            #heading{
                border:1px solid #000;
                width: 100%%;
                height: 120px;
            }
            #content_menu{
                border:1px solid #000;
                width: 30%%;
                height: 700px;
                border-right: 0px;
                border-top: 0px;
                border-bottom: 0px;
                float: left;
            }
            #content_body{
                border:1px solid #000;
                width: 69%%;
                height: 700px;
                border-left: 0px;
                border-top: 0px;
                border-bottom: 0px;
                float: right;
            }
            #floor{
                border:1px solid #000;
                clear: both;
            }
            table{font-size:13px;}
            input#intest{
                font-weight:bold;
            } 
        </style>
    <script language="javascript" type="text/javascript">
        var row_array = new Array() 
        var btn_array = new Array()
        function removeByValue(arr, val){
            for(var i=0; i<arr.length;i++){
                if(arr[i] == val){
                    arr.splice(i,1);
                    break;
                }
            }
        }
        function setDetailMsgRow(rowID, btn) {  
            for (n in rowID){
                var row = document.getElementById(rowID[n]);  
                if (row != null) {  
                    if (row.style.display == (document.all ? "block" : "table-row")) {  
                        row.style.display = "none";  
                        btn.style.color='black';
                        removeByValue(row_array, rowID[n])
                        removeByValue(btn_array, btn)
                    }  
                    else {  
                        row.style.display = (document.all ? "block" : "table-row");
                        btn.style.color='orange';  
                        row_array.push(rowID[n])
                        btn_array.push(btn)
                    }  
                }
            } 
            if (btn != null){
                if (btn.value != "Show Detail"){
                    btn.value = "Show Detail"
                }else{
                    btn.value = "Hide"
                }
            }  
        }
        function showRow(a, btn) { 
            var arr = new Array()
            var row_arr = new Array()
            for (i=0;i<a[1];i++ ){
                arr[i] = ("if"+a[0]+"-") + (i+1)
                row_arr[i] = ("row"+a[0]+"-") + (i+1)
                }
            for (rowID in arr){
                var row = document.getElementById(arr[rowID]);  
                if (row != null) {  
                    if (row.style.display == (document.all ? "block" : "table-row")) {  
                        row.style.display = "none";  
                        btn.style.color='black';
                        if (row_array.length > 0){
                            for (j in row_array){
                                if(row_array[j] == row_arr[rowID]){
                                    var row_case = document.getElementById(row_array[j])
                                    row_case.style.display="none"
                                    var param_row = document.getElementById(row_array[j]+'-'+1)
                                    param_row.style.display="none"
                                    btn_array[j].style.color = "black"
                                    btn_array[j].value = "Show Detail"
                                    btn_array.splice(j,1)
                                    row_array.splice(j,1)
                                }
                            }                            
                        }
                    }  
                    else {  
                        row.style.display = (document.all ? "block" : "table-row");
                        btn.style.color='brown';  
                    }  
                } 
            
            }
            if (btn != null){
                if (btn.value != "查看详情"){
                    btn.value = "查看详情"
                }else{
                    btn.value = "收起"
                }
            } 
        } 
function FillRect(cxt, x1, y1, width, height, color) {
    cxt.fillStyle = color;
    cxt.fillRect(x1, y1, width, height);
}
function drawBar(pass, fail, error){
 
    var color = ["#6c6","orchid","#c00"]; 
    var data = [pass,fail,error];
    var count = pass + fail + error;
    var h =[10+(1 - pass/count)*148,10+(1 - fail/count)*148,10+(1 - error/count)*148];
    var x = [30,90,150];
    var y = [70,130,190];
    var canvas = document.getElementById("bar"); 
    var ctx = canvas.getContext("2d");
    DrawString(ctx, 'Count(c)', '', '', '', '', 15, 10)
    DrawLine(ctx,5,15,10,10,'black');
    DrawLine(ctx,15,15,10,10,'black');
    DrawLine(ctx,10,10,10,158,'black');
    DrawLine(ctx,10,158,215,158,'black');
    DrawLine(ctx,210,153,215,158,'black');
    DrawLine(ctx,210,163,215,158,'black');
    DrawString(ctx, 'Type(c)', '', '', '', '', 180, 160)
    for(var i=0;i<3;i++) {
        DrawLine(ctx,x[i],h[i],x[i],158,color[i]);
        DrawLine(ctx,x[i],h[i],y[i],h[i],color[i]);
        DrawLine(ctx,y[i],h[i],y[i],158,color[i]);
        DrawLine(ctx,(y[i]+x[i])/2,153,(y[i]+x[i])/2,158,color[i]);
        DrawString(ctx, data[i], '', color[i], '', '', (y[i]+x[i])/2, h[i]-15);
        FillRect(ctx, x[i], h[i], 40, 158-h[i], color[i]);
    }
}
 
function DrawLine(cxt, x1, y1, x2, y2, color) {
 
    cxt.strokeStyle = color;
    cxt.beginPath();
    cxt.moveTo(x1, y1);
    cxt.lineTo(x2, y2);
    cxt.stroke();
}
 
function DrawString(cxt, text, font, color, align, v_align, x, y) {
    if (font == "") {
        cxt.font = "10px";
    }
    else {
        cxt.font = font;
    }
    if (color == "") {
        cxt.fillStyle = "#000000";
    }
    else {
        cxt.fillStyle = color;
    }
    if (align == "") {
        cxt.textAlign = "left";
    }
    else {
        cxt.textAlign = align;
    }
    if (v_align == "") {
        cxt.textBaseline = "top";
    }
    else {
        cxt.textBaseline = v_align;
    }
    cxt.fillText(text, x, y);
}
 

    </script> 
</head>

<body>
    <div id="heading" style="background:#DBDBDB">
    <p style="font-family:verdana;color:black;font-size:18"><B>Project:  "%s"  Interface Test Report</B></p>
        <p style="font-family:verdana;color:black;font-size:13px;">       
        测试套件总数：%s，用例总数：%s，成功：%s，失败：%s， 错误：%s。</p>
        <p style="font-family:verdana;color:black;font-size:13px;">       
        执行时间：%s， 运行时长：%.6f s </p>
    </div>
    <div id="left-body" style="overflow:auto;">
        <table  width="100%%" border="1" cellpadding="0" cellspacing="0" style="table-layout:fixed" bgcolor="#FAFAFA">
            <tr align="center" >
                <td width="25%%" align="left" style="font-family:verdana;color:blue;font-size:14"><B>Test Case</B></td> 
                <td width="7%%" style="font-family:verdana;color:blue;font-size:16"><B>Time</B></td> 
                <td width="7%%" style="font-family:verdana;color:blue;font-size:16"><B>Result</B></td> 
                <td width="44%%" style="font-family:verdana;color:blue;font-size:16"><B>Result Message</B></td> 
                <td width="15%%" style="font-family:verdana;color:blue;font-size:16"><B>Detail</B></td> 
            </tr>
            %s  
        </table>
    </div> 
    <div id="floor">
        <div class="barchart"> 
        <p> 测试结果统计图： <button style='color:green'onclick='javascript:drawBar(%s, %s, %s)' >Show Chart</button></p>
        <canvas id="bar" width="225" height="168" >your browser does not support the canvas tag</canvas>
        </div>
    <!-- <p> 测试结果统计图： <button style='color:green' onclick="setDetailMsgRow('img1',this)">Show Chart</button></p>      
    <img id='img1' style="display:none" src="./chart.png"/> -->
    </div>
</body>
</html> """ % (self.prj_name, self.if_total, self.pass_num+self.fail_num+self.un_num,
               self.pass_num, self.fail_num, self.un_num,
               time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), self.total_time, self.if_html,
               self.pass_num, self.fail_num, self.un_num)
        try:
            draw_chart.draw([self.pass_num, self.fail_num, self.un_num], self.report_path)
            with open(self.report_path+'/Report.html', 'w', encoding="UTF-8") as f:
                f.write(html)
        except Exception:
            self.logger.error(traceback.format_exc())

