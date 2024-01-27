// Copy to Clipboard
const copyTextToClipboard = (text) => {
	console.log("IN");
	if (navigator.clipboard) {
		navigator.clipboard
			.writeText(text)
			.then(() => {
				Toastify({
					text: "Post link copied to clipboard!",
					duration: 5000,
					gravity: "top",
					position: "center",
				}).showToast();
			})
			.catch((err) => {
				Toastify({
					text: "Something went wrong! Please try again.",
					duration: 5000,
					gravity: "top",
					position: "center",
					backgroundColor: "#fca5a5",
				}).showToast();
			});
	}
};

// Red borders and small text errors instead of default error messages
$("input, textarea").on("invalid", (event) => {
	event.preventDefault();
});
$("input, textarea").on("keyup focusout invalid", (event) => {
	event.preventDefault();

	let waitTime = event.type === "invalid" ? 100 : 0;

	setTimeout(() => {
		const targetElement = event.target;

		const errorDivId = `${targetElement.id}-error`;
		const errorDivSelector = `#${errorDivId}`;
		const existingErrorDiv = $(errorDivSelector);

		existingErrorDiv.remove();

		if (targetElement.checkValidity()) {
			targetElement.classList.remove("border-error");
		} else {
			targetElement.classList.add("border-error");

			let errorMessage = targetElement.validationMessage;

			const errorDiv = document.createElement("div");
			errorDiv.id = errorDivId;

			errorDiv.classList.add("text-error", "text-sm", "pt-1");
			if (targetElement.type === "file") {
				errorDiv.classList.add("text-center");
			}
			if (
				errorMessage.indexOf("Please include an '@'") > -1 ||
				errorMessage.indexOf("Please enter a part following '@'") > -1
			) {
				errorMessage = "Invalid email address.";
			}

			errorDiv.textContent = errorMessage;
			event.target.parentNode.appendChild(errorDiv);
		}
	}, waitTime);
});
