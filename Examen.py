from flask import Flask, render_template, request, redirect
from compras import compras_netas, costo_de_venta

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/inicialpage')


@app.route('/inicialpage')
def select_page() -> 'html':
    return render_template('inicialpage.html',
                           the_title='Seleccione es calculo deseado')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title= 'Calculo de Compras netas')


@app.route('/compras_netas', methods=["POST"])
def calcular() -> 'html':
    compras_totales = float(request.form['cpt'])
    devoluciones = float(request.form['dev'])
    descuentos = float(request.form['des'])
    results = compras_netas(compras_totales, devoluciones, descuentos)
    return render_template('results.html',
                           the_title='Bienvenido al calculo de compras netas',
                           the_comp_tot=compras_totales,
                           the_dev=devoluciones,
                           the_des = descuentos,
                           the_results= results,
                           )
@app.route('/entry1')
def entry_page1() -> 'html':
    return render_template('entry1.html',
                           the_title= 'Calculo de Costo de Ventas')

@app.route('/costo_de_venta', methods=["POST"])
def calcular1() -> 'html':
    compras_netas = float(request.form['cn'])
    inventario_inicial = float(request.form['in'])
    results = costo_de_venta(compras_netas, inventario_inicial)
    return render_template('results1.html',
                           the_title='Bienvenido al calculo de costo de ventas',
                           the_compras_netas=compras_netas,
                           the_inventario_inicial=inventario_inicial,
                           the_results=results,
                           )


if __name__ == '__main__':
    app.run()
