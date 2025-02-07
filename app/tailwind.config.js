/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./rodeland/templates/*.html"],
  theme: {
    extend: {
        screens: {
            // 'xl': '1024px',
            // '2xl': '1024px',
            '2xl': '1280px',
        },
        colors: {
          rodeland: {
            1: '#004434',
            2: '#80B687',
            3: '#F5906D',
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
