import React from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom'

import Home from './components/Pages/Home'

export default function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                {/* se liga no 'exact' */}
                {/* <Route path="/" exact component={Logon} /> */}

                <Route path="/" exact component={Home} />

            </Switch>
        </BrowserRouter>
    )
}