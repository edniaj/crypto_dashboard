import React, { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'

export async function getServerSideProps() {

  const resp = await fetch(`https://jherr-pokemon.s3.us-west-1.amazonaws.com/index.json`)

  return {
    props: {
      pokemon: await resp.json()
    }
  }
}

export default function Home({ pokemon }) {
  const base_url = `https://jherr-pokemon.s3.us-west-1.amazonaws.com/`
  return (
    <div className="container">
      <h2>Pokemon List</h2>
      {pokemon.map((pokemon) => (
        <div>
          <div>
            <img
              src={base_url + pokemon.image}
              style={{ height: '50px' }}
            />
          </div>
          <div>
            {JSON.stringify(pokemon)}
          </div>
        </div>
      ))}
    </div>
  )
}
