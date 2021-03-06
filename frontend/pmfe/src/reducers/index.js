import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'

import auth, * as fromAuth from './auth.js'
import echo, * as fromEcho from './echo.js'
import api, * as fromApi from './api.js'
import gui, * as fromGui from './gui.js'

export default combineReducers({
  auth: auth,
  echo: echo,
  api: api,
  gui: gui,
  router: routerReducer
})

export const isAuthenticated = state => fromAuth.isAuthenticated(state.auth)
export const accessToken = state => fromAuth.accessToken(state.auth)
export const isAccessTokenExpired = state => fromAuth.isAccessTokenExpired(state.auth)
export const refreshToken = state => fromAuth.refreshToken(state.auth)
export const isRefreshTokenExpired = state => fromAuth.isRefreshTokenExpired(state.auth)
export const authErrors = state => fromAuth.errors(state.auth)

export const serverProductsAll = state => fromApi.serverProductsAll(state.api)

export const serverMessage = state => fromEcho.serverMessage(state.echo)

export const mainView = state => fromGui.mainView(state.gui)

export function withAuth (headers = {}) {
  return (state) => ({
    ...headers,
    'Authorization': `Bearer ${accessToken(state)}`
  })
}
