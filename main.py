from flask import Flask, request, render_template, redirect, url_for, flash


app = Flask( __name__)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/temario')
def temario():
    return render_template('temario.html')

@app.route('/student')
def users():
    return render_template('student.html')

@app.route('/cap1/<int:id>', methods=['POST', 'GET'])
def cap1(id):
    #"1BmEQMd_4TrFiaDhVTlTPKX2Y24N9irmX",
    ARC = [0,
         "1BdC35tVBVQxwIhOoooJBxOhVw9uGwIjF",
         "14DUksLLCNvr8MuNH6F0dr-iI9BX-1tCR",
           "1IExnMaGzqCpxMWFVOCcKTEBU6Q-wiXPG", 
           "1zRi2SI8Lmk1_5sDoiAOwPdjyL5ZP-gjd",
            "1spMufq9N07gBq89WSB3QuCa3l2de47pe", 
            "1b84kxLVzay_JlV2dtyiS7_VYLNsh6hLk", 
            ]
    return render_template('CAP/cap1.html', contact=ARC[id])

@app.route('/cap2/<int:id>', methods=['POST', 'GET'])
def cap2(id):
    ARC = [0, 
           "1DOq5zm_5PtLYzgC60_txJ11CgWEoDBTx", 
           "1OMnI61LR67aIeq3EyIsmNj-DbwHeHyfP", 
           "1dRORu2MqNIDPWo-C64qvkXHPKHR3So9l", 
           "1HpZ_SHJLGRnOP3Zf4lQ5ezC8Dd_I3e2U"]
   
    return render_template('CAP/cap2.html', contact=ARC[id])

@app.route('/cap3/<int:id>', methods=['POST', 'GET'])
def cap3(id):

    ARC = [0, 
           "1x1NvUdJbdve_5k05rWwYh2Dmks5e3LbN",
           "1GYx-85wqpcD1mXGMqNjJAzv1o_UFxfSn",
           "1vtBITMLbdwRlxnZx6BXK-L0AJqJAYrf6",
           "1oIYO83Qr8T-xKjSHY7DvzVBeeYA35EO1",
           "11g5pO6_rg7Oj73uS3vkJiZRH8rtKnoBO"]
   
    return render_template('CAP/cap3.html', contact=ARC[id])

@app.route('/cap4/<int:id>', methods=['POST', 'GET'])
def cap4(id):


    ARC = [0, 
           "1b2CLU4fLiCDpDsutyc6Spgr3qeBAGKg8",
           "1hV1mW7BxQXgu3r6Z-RAh5uBlKNcYXxkH",
           "1QR_mO9QP_nYtULFWWMMEx_MJABfKfSgt",
           "1AR63mkLgyDu1tT9o48wn1Ckj9alOVEAL",
           "11g5pO6_rg7Oj73uS3vkJiZRH8rtKnoBO"]
   
    return render_template('CAP/cap4.html', contact=ARC[id])

@app.route('/cap5/<int:id>', methods=['POST', 'GET'])
def cap5(id):


    ARC = [0, 
           
           
           
           "1dYjBpEn35Y9OoIYZZi2vPfoAStgYhihO",
           "189rUIeLVAp0OEavs4ifk9iupuPJbzvK_",
           "1ZiDwtWLvMz8rfBsz8gGxaZq8bMbREIy3",
           "1FdTN_-eEBhSYbPGhJpCt4B2cbmoQ5ufb",
           "1a__gON5DI2vAqZllG7GiywizakSFl_qp",]
   
    return render_template('CAP/cap5.html', contact=ARC[id])

@app.route('/cap6/<int:id>', methods=['POST', 'GET'])
def cap6(id):


    ARC = [0, 
           
            "1SufFjt67nzZSIsIpds8ysf_Oaiu75Agw",
           
           "1KTYt8rnmNcOCF5YkUw07X2HFr3HXxVUI",
           "18G_BYaMAgUd6y1gD0OsMzR6JcUqBKHD8",
          "1n9zTs_HLxbncX7M1y0oC7NKUx6GGHzwi",
           "1idxdWhQcHk9c5GxY4VYpGRbv7VDqmCRj",
           "11g5pO6_rg7Oj73uS3vkJiZRH8rtKnoBO"]
    
   
    return render_template('CAP/cap6.html', contact=ARC[id])
@app.route('/VERPDF/<int:id>', methods=['POST', 'GET'])
def VERPDF(id):
    pdf = [0, 
           "1DcGzziQV6XO7EB92VNxSvOI8wfHz0L_D",
           "16_gYTZIDHc4nW1iYJa-7ZpMG945iCnRl",
           "116209125536641958645&rtpof"
           ]
    en=[0,
        "LABORATORIO 1 ",
        "LABORATORIO 2",
        "LABORATORIO 2"
        ]
    sub =[0,
         "MODELOS DE PROPAGACION",
         "RADIOELNACE RADIOWORKS",
         "ENLACE X-IRIO ONLINE"
         ]
   
 

    return render_template('CAP/VERPDF.html', pdf=pdf[id],en=en[id],sub=sub[id])


## llamada a manuales de usuario

@app.route('/software')
def software():
    return render_template('SOF/software.html')

@app.route('/descargas')
def descargas(): 
    
    return render_template('descargas.html')

## llamada a banco de preguntas y simulador
@app.route('/reactivos')
def banco():
    return render_template('EJE/reactivos.html')

@app.route('/ejercicios')
def ejercicios():
    return render_template('EJE/ejercicios.html')


## llamada los preparatorios
@app.route('/lab1')
def l1():
    return render_template('LAB/reactivos.html')

@app.route('/lab2')
def l2():
    return render_template('LAB/ejercicios.html')

@app.route('/extras')
def extras():
    return render_template('extras.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')


@app.route('/VER/<int:dat>', methods=['POST', 'GET'])
def ver(dat):
    vis=[0,
         "snq3e30zk06v",
         "vj16ydwgz3-h",
         "fkexpq5gukmq",
         "1mvoa7xsp0fr",
         "mqpwbbt4wgm3",
         "2gqvvgbvkeng",
         "2gqvvgbvkeng"

    ]
    cap=[0,
         "CAPITULO 1",
         "CAPITULO 2",
         "CAPITULO 3",
         "CAPITULO 4",
         "CAPITULO 5",
         "CAPITULO 6"
         
         ]

    return render_template('CAP/ver.html', capitulo=cap[dat], prezi=vis[dat])




if __name__ == "__main__":
    app.run(port=3000, debug=True, host="0.0.0.0")