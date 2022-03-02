'use strict';

module.exports = {
  /**
   * An asynchronous register function that runs before
   * your application is initialized.
   *
   * This gives you an opportunity to extend code.
   */
  register(/*{ strapi }*/) {},

  /**
   * An asynchronous bootstrap function that runs before
   * your application gets started.
   *
   * This gives you an opportunity to set up your data model,
   * run jobs, or perform some special logic.
   */
  bootstrap(/*{ strapi }*/) {
    module.exports = async () => {
      await strapi.admin.services.permission.conditionProvider.register({
        displayName: 'Billing amount under 10K',
        name: 'billing-amount-under-10k',
        plugin: 'admin',
        handler: { amount: { $lt: 10000 } },
      });
    };
  },
};

