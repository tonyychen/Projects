park_urls = [
    #Acadia
    'https://www.tripadvisor.com/Attraction_Review-g60709-d12785836-Reviews-Acadia_National_Park-Bar_Harbor_Mount_Desert_Island_Maine.html',
    #American Samoa 
    'https://www.tripadvisor.com/Attraction_Review-g60672-d6776101-Reviews-National_Park_of_American_Samoa-Pago_Pago_Tutuila.html',
    #Arches
    'https://www.tripadvisor.com/Attraction_Review-g60724-d8535374-Reviews-Arches_National_Park-Moab_Utah.html',
    #Badlands
    'https://www.tripadvisor.com/Attraction_Review-g60729-d10212205-Reviews-Badlands_National_Park-Interior_South_Dakota.html',
    #Big Bend: N/A
    #Biscayne: N/A
    #Black Canyon of the Gunnison
    'https://www.tripadvisor.com/Attraction_Review-g143014-d145009-Reviews-Black_Canyon_Of_The_Gunnison_National_Park-Black_Canyon_Of_The_Gunnison_National_P.html',
    #Bryance Canyon
    'https://www.tripadvisor.com/Attraction_Review-g143015-d1925256-Reviews-Bryce_Canyon_National_Park-Bryce_Canyon_National_Park_Utah.html',
    #Canyonlands
    'https://www.tripadvisor.com/Attraction_Review-g60724-d8837806-Reviews-Canyonlands_National_Park-Moab_Utah.html',
    #Capitol Reef
    'https://www.tripadvisor.com/Attraction_Review-g143017-d212117-Reviews-Capitol_Reef_National_Park-Capitol_Reef_National_Park_Utah.html',
    #Carlsbad Caverns: N/A
    #Channel Islands: N/A
    #Congaree
    'https://www.tripadvisor.com/Attraction_Review-g60777-d143108-Reviews-Congaree_National_Park-Hopkins_South_Carolina.html',
    #Crater Lake
    'https://www.tripadvisor.com/Attraction_Review-g143020-d144747-Reviews-Crater_Lake_National_Park-Crater_Lake_National_Park_Oregon.html',
    #Cuyahoga Valley
    'https://www.tripadvisor.com/Attraction_Review-g60784-d261325-Reviews-Cuyahoga_Valley_National_Park-Brecksville_Ohio.html',
    #Death Valley: N/A
    #Denali
    'https://www.tripadvisor.com/Attraction_Review-g28923-d144478-Reviews-Denali_National_Park-Alaska.html',
    #Dry Torgulas
    'https://www.tripadvisor.com/Attraction_Review-g34345-d3417409-Reviews-Dry_Tortugas_National_Park-Key_West_Florida_Keys_Florida.html',
    #Everglades
    'https://www.tripadvisor.com/Attraction_Review-g34225-d6851227-Reviews-Everglades_National_Park-Florida_City_Florida.html',
    #Gates of the Arctic: N/A
    #Gateway Arch
    'https://www.tripadvisor.com/Attraction_Review-g44881-d104318-Reviews-The_Gateway_Arch-Saint_Louis_Missouri.html',
    #Glacier
    'https://www.tripadvisor.com/Attraction_Review-g60832-d14208544-Reviews-Glacier_National_Park-West_Glacier_Montana.html',
    #Glacier Bay
    'https://www.tripadvisor.com/Attraction_Review-g143027-d537964-Reviews-Glacier_Bay_National_Park_Preserve-Glacier_Bay_National_Park_and_Preserve_Alaska.html',
    #Grand Canyon
    'https://www.tripadvisor.com/Attraction_Review-g143028-d12235326-Reviews-Grand_Canyon_National_Park-Grand_Canyon_National_Park_Arizona.html',
    #Grand Teton
    'https://www.tripadvisor.com/Attraction_Review-g143029-d145270-Reviews-Grand_Teton-Grand_Teton_National_Park_Wyoming.html',
    #Great Basin
    'https://www.tripadvisor.com/Attraction_Review-g60840-d1584499-Reviews-Great_Basin_National_Park-Baker_Nevada.html',
    #Great Sand Dunes
    'https://www.tripadvisor.com/Attraction_Review-g60841-d9800243-Reviews-Great_Sand_Dunes_National_Park-Mosca_Colorado.html',
    #Great Smoky Mountains
    'https://www.tripadvisor.com/Attraction_Review-g60842-d12833528-Reviews-Great_Smoky_Mountains_National_Park-Gatlinburg_Tennessee.html',
    #Guadalupe Mountains
    'https://www.tripadvisor.com/Attraction_Review-g60844-d8064236-Reviews-Guadalupe_Mountains_National_Park-Salt_Flat_Texas.html',
    #Haleakala
    'https://www.tripadvisor.com/Attraction_Review-g60633-d2077822-Reviews-Haleakala_National_Park-Kula_Maui_Hawaii.html',
    #Hawaii Vocanoes
    'https://www.tripadvisor.com/Attraction_Review-g143034-d1603722-Reviews-Hawaii_Volcanoes_National_Park-Hawaii_Volcanoes_National_Park_Island_of_Hawaii_Ha.html',
    #Hot Springs
    'https://www.tripadvisor.com/Attraction_Review-g60856-d3224470-Reviews-Hot_Springs_National_Park-Hot_Springs_Arkansas.html',
    #Indiana Dunes
    'https://www.tripadvisor.com/Attraction_Review-g60861-d5990503-Reviews-Indiana_Dunes_National_Park-Porter_Indiana.html',
    #Isle Royale: N/A
    #Joshua Tree
    'https://www.tripadvisor.com/Attraction_Review-g32544-d13955290-Reviews-Joshua_Tree_National_Park-Joshua_Tree_California.html',
    #Katmai: N/A
    #Kenai Fjords
    'https://www.tripadvisor.com/Attraction_Review-g60873-d3377126-Reviews-Kenai_Fjords_National_Park-Seward_Alaska.html',
    #Kings Canyon
    'https://www.tripadvisor.com/Attraction_Review-g143050-d145249-Reviews-Kings_Canyon-Sequoia_and_Kings_Canyon_National_Park_California.html',
    #Kobuk Valley
    'https://www.tripadvisor.com/Attraction_Review-g143040-d12268414-Reviews-Kobuk_Valley_National_Park-Kobuk_Valley_National_Park_Alaska.html',
    #Lake Clark
    'https://www.tripadvisor.com/Attraction_Review-g143041-d12268413-Reviews-Lake_Clark_National_Park_and_Preserve-Lake_Clark_National_Park_and_Preserve_Alas.html',
    #Lassen Volcanic: N/A
    #Mammoth Cave: N/A
    #Mesa Verde
    'https://www.tripadvisor.com/Attraction_Review-g60900-d14788340-Reviews-Mesa_Verde_National_Park-Mesa_Verde_National_Park_Colorado.html',
    #Mount Rainier: N/A
    #North Cascades
    'https://www.tripadvisor.com/Attraction_Review-g143046-d12409123-Reviews-North_Cascades_National_Park-North_Cascades_National_Park_Washington.html',
    #Olympic: N/A
    #Petrified Forest
    'https://www.tripadvisor.com/Attraction_Review-g31244-d10634539-Reviews-Petrified_Forest_National_Park-Holbrook_Arizona.html',
    #Pinnacles
    'https://www.tripadvisor.com/Attraction_Review-g60935-d143240-Reviews-Pinnacles_National_Park-Paicines_California.html',
    #Redwood
    'https://www.tripadvisor.com/Attraction_Review-g2193168-d210214-Reviews-Redwood_National_Park-Redwood_National_Park_California.html',
    #Rocky Mounain: N/A
    #Saguaro
    'https://www.tripadvisor.com/Attraction_Review-g60950-d12704675-Reviews-Saguaro_National_Park-Tucson_Arizona.html',
    #Sequoia
    'https://www.tripadvisor.com/Attraction_Review-g33230-d12902316-Reviews-Sequoia_National_Park-Visalia_California.html',
    #Shenandoah: N/A
    #Theodore Roosevelt
    'https://www.tripadvisor.com/Attraction_Review-g60973-d1911641-Reviews-Theodore_Roosevelt_National_Park-Medora_North_Dakota.html',
    #Virgin Islands: N/A
    #Voyageurs
    'https://www.tripadvisor.com/Attraction_Review-g43447-d12659479-Reviews-Voyageurs_National_Park-Ray_Minnesota.html',
    #White Sands
    'https://www.tripadvisor.com/Attraction_Review-g28952-d103700-Reviews-White_Sands_National_Monument-New_Mexico.html',
    #Wind Cave
    'https://www.tripadvisor.com/Attraction_Review-g143055-d10162780-Reviews-Wind_Cave_National_Park-Wind_Cave_National_Park_South_Dakota.html',
    #Wrangell–St. Elias: N/A
    #Yellowstone
    'https://www.tripadvisor.com/Attraction_Review-g60999-d12235309-Reviews-Yellowstone_National_Park-Yellowstone_National_Park_Wyoming.html',
    #Yosemite: N/A
    #Zion
    'https://www.tripadvisor.com/Attraction_Review-g143057-d10035237-Reviews-Zion_National_Park-Zion_National_Park_Utah.html'
]