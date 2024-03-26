/**
 * User Prompt: A computed property name in a type literal must refer to an expression whose type is a literal type or a 'unique symbol' type.
 */

const SCREEN_KEYS = {
  Landing: 'Landing',
  Login: 'Login' ,
  Intro: 'Intro' ,}


const SCREEN_KEYS = {
Landing: 'Landing' as const,
Login: 'Login' as const,
Intro: 'Intro' as const,}