from flask import Flask, render_template, redirect, request
import mariadb

app = Flask(__name__)

# conexión a base de datos
def conectar():
    return mariadb.connect(
        user="marta",
        password="marta.21",
        host="localhost",
        database="CentroAdopcion"
    )

# página principal
@app.route("/")
def home():
    return redirect("/catalogo")

# catálogo de perros
@app.route("/catalogo")
def catalogo():

    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT id, name, age, adopted, breed FROM Dog")
    rows = cur.fetchall()

    perros = []

    for row in rows:
        perros.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "adopted": row[3],
            "breed": row[4]
        })

    conn.close()

    mensaje = False
    if request.args.get("ok"):
        mensaje = True

    return render_template("catalogo.html", dogs=perros, mensaje=mensaje)

# adoptar perro
@app.route("/adoptar/<int:dog_id>")
def adoptar(dog_id):

    conn = conectar()
    cur = conn.cursor()

    cur.execute("UPDATE Dog SET adopted = 1 WHERE id = ?", (dog_id,))
    conn.commit()

    conn.close()

    return redirect("/catalogo?ok=1")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    