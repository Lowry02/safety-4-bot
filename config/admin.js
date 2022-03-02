module.exports = ({ env }) => ({
  auth: {
    secret: env('ADMIN_JWT_SECRET', 'c7c46d78fe6804060cbb8bc72ed5d56f'),
  },
});
