const baseUrl = 'https://covid19.mathdro.id/api/daily';
const getDaily = async(tanggal) => {
    try {
        const response = await get(`${baseUrl}/${tanggal}`);
        const responseJson = await response.json();
        const yukBisaYuk = await responseJson.forEach(daily => {
            if (daily.countryRegion == 'Indonesia') {
                let data = parseInt(daily.confirmed);
                arr.push(data);
                return data;
            }
        });

    } catch (error) {
        console.log(error);
    }
}
const arr = [];
const now = new Date();
for (let d = new Date(2020, 3, 10); d <= now; d.setDate(d.getDate() + 2)) {
    const date = new Date(d);
    const mm = date.getMonth() + 1;
    const dd = date.getDate();
    const yy = date.getFullYear();
    getDaily(`${mm}-${dd}-${yy}`);

    function set(data) {
        setTimeout(function() {
            console.log(data);
            arr.push(data);
        }, 2000)
    }
};
console.log('ini arr', arr);