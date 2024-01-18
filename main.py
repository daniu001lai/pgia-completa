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
            "1F-ai_n29EkXrMIR02IjyRzw2BTUNU7WP", 
            ]
    return render_template('CAP/cap1.html', contact=ARC[id])

@app.route('/cap2/<int:id>', methods=['POST', 'GET'])
def cap2(id):
    ARC = [0, 
           "1DOq5zm_5PtLYzgC60_txJ11CgWEoDBTx", 
           "1OMnI61LR67aIeq3EyIsmNj-DbwHeHyfP", 
           "1dRORu2MqNIDPWo-C64qvkXHPKHR3So9l", 
           "1BUBUEyL4Gf_elSH91-ZnB33GGv__8H-f"]
   
    return render_template('CAP/cap2.html', contact=ARC[id])

@app.route('/cap3/<id>', methods=['POST', 'GET'])
def cap3(id):
    ARC = [0, 
           "b2CLU4fLiCDpDsutyc6Spgr3qeBAGKg8",
           "1hV1mW7BxQXgu3r6Z-RAh5uBlKNcYXxkH",
           "1QR_mO9QP_nYtULFWWMMEx_MJABfKfSgt",
           "1AR63mkLgyDu1tT9o48wn1Ckj9alOVEAL",
           ""]
   
    return render_template('CAP/cap2.html', contact=ARC[id])

@app.route('/cap4/<id>', methods=['POST', 'GET'])
def cap4(id):

    ARC = [0, 
           "b2CLU4fLiCDpDsutyc6Spgr3qeBAGKg8",
           "1hV1mW7BxQXgu3r6Z-RAh5uBlKNcYXxkH",
           "1QR_mO9QP_nYtULFWWMMEx_MJABfKfSgt",
           "1AR63mkLgyDu1tT9o48wn1Ckj9alOVEAL",
           ""]
   
    return render_template('CAP/cap2.html', contact=ARC[id])

@app.route('/cap5/<id>', methods=['POST', 'GET'])
def cap5(id):


    ARC = [0, 
           "1Nvy7h7m838kkyqS5pq4yz4B5OieUfb3O",
           "1FdTN_-eEBhSYbPGhJpCt4B2cbmoQ5ufb",
           "1ZiDwtWLvMz8rfBsz8gGxaZq8bMbREIy3",
           "189rUIeLVAp0OEavs4ifk9iupuPJbzvK_",
           "1dYjBpEn35Y9OoIYZZi2vPfoAStgYhihO"]
   
    return render_template('CAP/cap2.html', contact=ARC[id])

@app.route('/cap6/<id>', methods=['POST', 'GET'])
def cap6(id):


    ARC = [0, 
           "1Nvy7h7m838kkyqS5pq4yz4B5OieUfb3O",
           "1FdTN_-eEBhSYbPGhJpCt4B2cbmoQ5ufb",
           "1ZiDwtWLvMz8rfBsz8gGxaZq8bMbREIy3",
           "189rUIeLVAp0OEavs4ifk9iupuPJbzvK_",
           "1dYjBpEn35Y9OoIYZZi2vPfoAStgYhihO"]
   
    return render_template('CAP/cap2.html', contact=ARC[id])


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
    app.run(host="0.0.0.0")