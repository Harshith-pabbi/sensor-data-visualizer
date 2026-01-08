class ThemeEngine:
    THEMES = {
        'dark': {'bg': '#0f172a', 'line': 'cyan'},
        'light': {'bg': 'white', 'line': 'blue'},
        'neon': {'bg': 'black', 'line': 'lime'}
    }
    
    def __init__(self):
        self.current = 'dark'
    
    def apply(self, plt):
        theme = self.THEMES[self.current]
        plt.style.use('default')
        plt.gca().set_facecolor(theme['bg'])
        return theme['line']
    
    def switch(self, name):
        if name in self.THEMES:
            self.current = name
