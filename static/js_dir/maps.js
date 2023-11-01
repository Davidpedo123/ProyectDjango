var map;
function loadMapScenario() {
    map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
        credentials: 'YouKeyApi'
    });
    map.setView({ center: new Microsoft.Maps.Location(47.6149, -122.1941), zoom: 10 });
}
