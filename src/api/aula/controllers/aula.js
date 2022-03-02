'use strict';

/**
 *  aula controller
 */

let moment = require('moment')

const { createCoreController } = require('@strapi/strapi').factories;
const { convertRestQueryParams, buildQuery } = require("strapi-utils");

module.exports = createCoreController('api::aula.aula', ({strapi}) => ({

    async prova(ctx) {
        console.log(await strapi.db.query('plugin::users-permissions.user').findMany({select:['password']})[0])
        return 'bella'
    },

    async find(ctx) {
        let userId = ctx.state.auth.credentials.id
        let response = await strapi.db.query('plugin::users-permissions.user').findOne({ populate : true, where : { id : userId } })
        if(response != null) {
            // USER REQUEST
            userId = response.admin_user.id
            response = await strapi.db.query('api::aula.aula').findMany({where : { admin_user : userId } })

        } else {
            // API TOKEN
            let dayOfWeek = {
                0 : "Domenica",
                1 : "Lunedì",
                2 : "Martedì",
                3 : "Mercoledì",
                4 : "Giovedì",
                5 : "Venerdì",
                6 : "Sabato",
            }
            let tomorrow = moment().add(1, 'day').format('d')
            tomorrow = dayOfWeek[tomorrow]
            response = await strapi.db.query('api::aula.aula').findMany({where: {'Giorno' : {"Nome" : tomorrow}} ,populate : {admin_user : { select : ['id']}, Giorno : {select : ['Nome']}}})
            for(let item of response) {
                let adminUserId = response.adminUserId
                let userInfo = await strapi.db.query('plugin::users-permissions.user').findOne(adminUserId)
                let userPassword = userInfo.clear_password
                let userUsername = userInfo.username
                let hour = moment(item['Ora'], "HH:mm:ss.sss").format("HH") + "00"
                item['Ora'] = hour
                item['esse3username'] = userUsername
                item['esse3psw'] = userPassword
                delete item['admin_user']
            }
        }
        return response
    }

}));
