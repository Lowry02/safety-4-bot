"use strict"

module.exports = {
    routes: [
        {
            method: "GET",
            path: "/aula/prova",
            handler: ("aula.prova"),
            config: {
                policies: []
            }
        }
    ]
}