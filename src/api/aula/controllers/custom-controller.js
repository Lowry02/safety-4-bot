const { createCoreController } = require("@strapi/strapi").factories 
const moduleUid = "api::aula.aula"

module.exports = createCoreController(moduleUid, ({ strapi }) => ({

    async prova(ctx) {
        console.log('wow')
        return 'ciao'
    } 
    
}))