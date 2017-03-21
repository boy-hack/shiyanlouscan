import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class outputer:
    data = {}

    def get(self,key):
        if key in self.data:
            return self.data[key]
        return None

    def add(self,key,data):
        self.data[key] = data

    def add_list(self,key,data):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(data)

    def show(self):
        for key in self.data:
            print "%s:%s"%(key,self.data[key])
    
    def _build_table(self):
        _str = ""
        for key in self.data:
            if isinstance(self.data[key],list):
                _td = ""
                for key2 in self.data[key]:
                    _td += key2 + '</br>'
                _str += "<tr><td>%s</td><td>%s</td></tr>"%(key,_td)
            else:
                _str += "<tr><td>%s</td><td>%s</td></tr>"%(key,self.data[key])
        return _str
    def build_html(self,filename):
        html_head = '''
        <!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="gbk">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>W8ayscan Report</title>
<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
<div class="container container-fluid">
	<div class="row-fluid">
		<div class="span12">
			<h3 class="text-center">
				W8ayscan Report
			</h3>
			</BR>
			<table class="table table-bordered">
				<thead>
					<tr>
						<th>
							title
						</th>
						<th>
							content
						</th>
					</tr>
				</thead>
				<tbody>
					build_html_w8ayScan
				</tbody>
			</table>
		</div>
	</div>
</div>  </body>
</html>'''.replace("build_html_w8ayScan",self._build_table())
        file_object = open(filename+'.html', 'w')
        file_object.write(html_head)
        file_object.close()