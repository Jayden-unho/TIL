export const setStorage = (key, value) => {
  try {
    if (value !== String) {
      value = JSON.stringify(value)
    }
    localStorage.setItem(key, value)
  } catch (error) {
    console.error(error)
  }
}

export const getStorage = key => {
  try {
    const stringValue = localStorage.getItem(key)
    
    if (stringValue === null) {
      return null
    } else if (stringValue === '') {
      return ''
    }
    
    const objectValue = JSON.parse(stringValue)
    return objectValue
  } catch (error) {
    console.error(error)
  }
}