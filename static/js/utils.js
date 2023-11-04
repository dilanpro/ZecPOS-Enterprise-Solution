const convertToLocale = (utcTimestamp) => {
	const utcDate = new Date(utcTimestamp * 1000);
	const localDate = new Date(utcDate.toLocaleString());

	const options = {
		year: "numeric",
		month: "short",
		day: "numeric",
		hour: "2-digit",
		minute: "2-digit",
		second: "2-digit",
	};
	const formattedDate = new Intl.DateTimeFormat(undefined, options).format(
		localDate
	);

	return formattedDate;
};
