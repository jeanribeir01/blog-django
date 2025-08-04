/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './djangoapp/templates/**/*.html',
    './djangoapp/**/templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
}