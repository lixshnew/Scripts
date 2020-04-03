del win_tags 
del win_cscope.out
ctags -R -f .\win_tags *
cscope -Rb -f .\win_cscope.out 