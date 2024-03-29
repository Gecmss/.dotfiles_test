return require('packer').startup(function()
    -- Packer can manage itself as an optional plugin
    use {'wbthomason/packer.nvim', opt = true}

    -- Startify
    -- use { 'mhinz/vim-startify' }.setup(require'alpha.themes.dashboard'.config)

    -- Dashboard
    use {
        'goolord/alpha-nvim',
        requires = { 'kyazdani42/nvim-web-devicons' },
        config = function ()
            require'plug_conf.alpha'
        end,
    }

    -- Devicons
    use { 'ryanoasis/vim-devicons' }

    -- Color scheme
    use { 'pineapplegiant/spaceduck' }
    use { 'folke/tokyonight.nvim' }
    use { 'folke/lsp-colors.nvim' }
    use {
        'mcchrish/zenbones.nvim',
        requires = {
            'rktjmp/lush.nvim'
        }
    }
    use {
        'RRethy/vim-hexokinase',
        run = 'make hexokinase',
        config = function()
            vim.g.Hexokinase_highlighters = {'backgroundfull'}
            vim.g.Hexokinase_optInPatterns = {
                'full_hex', 'rgb', 'rgba', 'hsl', 'hsla'
            }
        end
    }

    -- Fuzzy finder
    use {
        'nvim-telescope/telescope.nvim',
        requires = {
            { 'nvim-lua/popup.nvim' },
            { 'nvim-lua/plenary.nvim' },
        }
    }
    use { 'nvim-telescope/telescope-project.nvim' }
    use { 'nvim-telescope/telescope-file-browser.nvim' }

    -- Comments
    use { 'tpope/vim-commentary' }

    --Indent sharkdp/fd
    use { 'Yggdroot/indentLine' }

    -- Nerd Tree
    use { 'preservim/nerdtree' }

    -- Treesitter
    -- use { 'nvim-treesitter/nvim-treesitter' }

    -- Dense Analysis
    use { 'dense-analysis/ale' }

    -- Vim Polyglot
    use { 'sheerun/vim-polyglot' }

    -- Lua development
    use { 'tjdevries/nlua.nvim' }

    -- Vim dispatch
    use { 'tpope/vim-dispatch' }

    -- Fugitive for Git
    use { 'tpope/vim-fugitive' }

    -- Airline
    use { 'vim-airline/vim-airline' }
    use { 'vim-airline/vim-airline-themes' }

    -- Toggleterm
    use {
        'akinsho/toggleterm.nvim',
        tag = 'v1.*',
    }

    use { 'mfussenegger/nvim-dap' }

    use {
        {
            "williamboman/nvim-lsp-installer",
            config = function ()
                require("nvim-lsp-installer").setup {}
            end
        },
        {
            "neovim/nvim-lspconfig",
            after = "nvim-lsp-installer",
            config = function()
                local lspconfig = require("lspconfig")
                lspconfig.sumneko_lua.setup {}
                --- ...
            end
        }
    }

    -- AutoCompletion
    use 'neovim/nvim-lsp'
    use 'hrsh7th/nvim-cmp' -- Autocompletion plugin
    use 'hrsh7th/cmp-nvim-lsp' -- LSP source for nvim-cmp
    use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip' -- Snippets plugin

end)
