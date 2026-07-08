import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', () => {
  // State
  const backgroundColor = ref('#FFFFFF')
  const buttonColor = ref('#000000')
  const buttonStyle = ref<'rounded' | 'pill' | 'soft'>('rounded')
  const fontFamily = ref('Inter')

  // Actions
  function setTheme(theme: {
    background_color?: string
    button_color?: string
    button_style?: 'rounded' | 'pill' | 'soft'
    font_family?: string
  }) {
    if (theme.background_color) backgroundColor.value = theme.background_color
    if (theme.button_color) buttonColor.value = theme.button_color
    if (theme.button_style) buttonStyle.value = theme.button_style
    if (theme.font_family) fontFamily.value = theme.font_family
  }

  function $reset() {
    backgroundColor.value = '#FFFFFF'
    buttonColor.value = '#000000'
    buttonStyle.value = 'rounded'
    fontFamily.value = 'Inter'
  }

  return {
    backgroundColor,
    buttonColor,
    buttonStyle,
    fontFamily,
    setTheme,
    $reset,
  }
})
