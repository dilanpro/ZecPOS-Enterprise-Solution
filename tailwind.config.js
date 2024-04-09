/** @type {import('tailwindcss').Config} */

const colors = require("tailwindcss/colors");

module.exports = {
	content: ["**/*.html", "*.html", "**/*.js", "*.js"],
	theme: {
		extend: {
			colors: {
				background: colors.white,
				primary: colors.slate[800],
				secondary: colors.slate[200],
				error: colors.red[400],
				success: colors.green[400],
				light: colors.white,
				dark: colors.slate[950],
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
