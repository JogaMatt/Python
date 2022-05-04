fetch("https://api.pokemontcg.io/v2/cards/")
    .then(response => response.json() )
    .then(coderData => console.log(coderData) )
    .catch(err => console.log(err) )

// Get all cards (will take awhile, automatically pages through data)
pokemon.card.all()
    .then((cards) => {
      console.log(cards[0].name) // "Blastoise"
    })

// Get a single page of cards
pokemon.card.where({ pageSize: 250, page: 1 })
  .then(result => {
      console.log(result.data[0].name) // "Blastoise"
  })

// Filter cards via query parameters
pokemon.card.all({ q: 'set.name:generations subtypes:mega' })
  .then(result => {
      console.log(result.data[0].name) // "Venusaur"
  })

// Order by release date (descending)
pokemon.card.all({ q: 'subtypes:mega', orderBy: '-set.releaseDate' })
  .then(result => {
      console.log(result.data[0].name)
  })