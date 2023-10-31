var map;
function loadMapScenario() {
    map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
        credentials: 'AoFC9aVEQpvtFDUfzCC0fjXzCF6LffemhEoORlI7hV2ZdtzBbFl44ZlnTjmHs1Ih'
    });
    map.setView({ center: new Microsoft.Maps.Location(47.6149, -122.1941), zoom: 10 });
}