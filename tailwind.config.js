/** @type {import('tailwindcss').Config} */

const colors = require("tailwindcss/colors");

module.exports = {
	content: ["**/*.html", "*.html"],
	theme: {
		extend: {
			colors: {
				"background-main": colors.zinc[200],
				"background-dark": colors.zinc[800],
				"background-dark-h": colors.zinc[900],
				primary: colors.blue[500],
				"primary-h": colors.blue[700],
				secondary: colors.slate[500],
				"secondary-h": colors.slate[700],
				light: colors.white,
				dark: colors.black,
			},
			fontFamily: {
				"logo-style": ["Luckiest Guy", "cursive"],
			},
		},
		screens: {
			sm: "480px",
			md: "768px",
			lg: "940px",
			xl: "1024px",
			"2xl": "1190px",
			"3xl": "1440px",
			"4xl": "1600px",
			"5xl": "1920px",
		},
	},
	plugins: [require("@tailwindcss/typography")],
};
