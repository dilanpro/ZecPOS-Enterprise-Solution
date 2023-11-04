/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["**/*.html", "**/*.js"],
	theme: {
		extend: {
			colors: {
				// Background Colors
				"background-main": "#e4e4e7",
				"background-dark": "#27272a",
				"background-dark-high": "#18181b",
				success: "#86efac",
				error: "#fca5a5",

				// Color Palletc
				light: "#fff",
				"light-high": "#e4e4e7",
				primary: "#3b82f6",
				"primary-high": "#1d4ed8",
				regular: "#64748b",
				"regular-high": "#334155",

				// Hero Colors
				black: "#000",
				indigo: "#6366f1",
				purple: "#a855f7",
				pink: "#ec4899",
			},
			fontFamily: {
				// Logo Font
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
