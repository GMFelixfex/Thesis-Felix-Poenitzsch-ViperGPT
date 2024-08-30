im = load_image('https://viper.cs.columbia.edu/static/images/kids_muffins.jpg')


testCommand = '''
def execute_command(image):     
    image_patch = ImagePatch(image)     
    kids_patches = image_patch.find("kid")     
    muffin_patches = image_patch.find("muffin")     
    if len(kids_patches) == 0 or len(muffin_patches) == 0:         
        return "I don\'t see any kids or muffins in the photo."     
    kid_count = len(kids_patches)     
    muffin_count = len(muffin_patches)     
    if kid_count > muffin_count:         
        return f"There are {kid_count} kids and only {muffin_count} muffins, so each kid can have at most one muffin."     
    else:         
        return f"Each kid can have {math.floor(muffin_count / kid_count)} muffins for it to be fair."
'''

im = load_image('https://viper.cs.columbia.edu/static/images/kids_muffins.jpg')

print("Precompiled: ", 1)
compiled_code = compile(testCommand, '<string>', 'exec')
print("Postcompiled: ", 1)
exec(compiled_code,globals())
print("Postexec: ", 1)
print(execute_command(im))
print("End: ", 1)









#query = 'How many muffins can each kid have for it to be fair?'

#show_single_image(im)
#code = get_code(query, "lm_studio")
#print("------------------")
#print(code)
#print("------------------")


#code = (
#    "def execute_command(image, my_fig, time_wait_between_lines, syntax) -> str:\n    image_patch = ImagePatch(image)\n    kid_patches = image_patch.find('kid')\n    muffin_patches = image_patch.find('muffin')\n    num_kids = len(kid_patches)\n    num_muffins = len(muffin_patches)\n    if num_kids > 0:\n        muffins_per_kid = num_muffins // num_kids\n        return str(muffins_per_kid)\n    else:\n        return 'No kids found in the image.'",
#    None
#)


#execute_code(code, im, show_intermediate_steps=True)





'''def execute_command2(image):        
    image_patch = ImagePatch(image)     
    kids_patches = image_patch.find("kid")     
    muffin_patches = image_patch.find("muffin")     
    if len(kids_patches) == 0 or len(muffin_patches) == 0:         
        return "I don\'t see any kids or muffins in the photo."     
    kid_count = len(kids_patches)     
    muffin_count = len(muffin_patches)     
    if kid_count > muffin_count:         
        return f"There are {kid_count} kids and only {muffin_count} muffins, so each kid can have at most one muffin."     
    else:         
        return f"Each kid can have {math.floor(muffin_count / kid_count)} muffins for it to be fair."
                                                                           
    image_patch = ImagePatch(image)                                                                           
    kids = image_patch.find("kid")                                                                            
    muffin_counts = []                                                                                        
    for kid in kids:                                                                                          
        muffins = kid.find("muffin")                                                                          
        if len(muffins) > 0:                                                                                  
            muffin_counts.append(len(muffins))                                                                
    return str(sum(muffin_counts)/len(kids))  
'''


#print(execute_command2(im))



#print('done')
"""def execute_command(image, my_fig, time_wait_between_lines, syntax) -> str:
    image_patch = ImagePatch(image)
    kid_patches = image_patch.find("kid")
    muffin_patches = image_patch.find("muffin")
    
    if len(kid_patches) == 0 or len(muffin_patches) == 0:
        return "Cannot determine without kids or muffins in the image."
    
    num_kids = len(kid_patches)
    num_muffins = len(muffin_patches)
    
    if num_kids == 0:
        return "No kids found in the image."
    if num_muffins == 0:
        return "No muffins found in the image."
    
    muffins_per_kid = num_muffins // num_kids
    return str(muffins_per_kid)  # Return the number of muffins each kid can have for it to be fair.

print(execute_command(im, None, 0, None))"""


code_l = '''def execute_command(image, my_fig, time_wait_between_lines, syntax) -> str:
    image_patch = ImagePatch(image)
    show_all(lineno=1,value=(image_patch),valuename='image_patch',fig=my_fig,console_in=console,time_wait_between_l
ines=time_wait_between_lines); CodexAtLine(1,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    kid_patches = image_patch.find('kid')
    show_all(lineno=2,value=(kid_patches),valuename='kid_patches',fig=my_fig,console_in=console,time_wait_between_l
ines=time_wait_between_lines); CodexAtLine(2,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    muffin_patches = image_patch.find('muffin')
    show_all(lineno=3,value=(muffin_patches),valuename='muffin_patches',fig=my_fig,console_in=console,time_wait_bet
ween_lines=time_wait_between_lines); CodexAtLine(3,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    show_all(lineno=4,value=(len(kid_patches)),valuename='len(kid_patches)',fig=my_fig,console_in=console,time_wait
_between_lines=time_wait_between_lines); 
CodexAtLine(4,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    show_all(lineno=4,value=(0 or len(muffin_patches)),valuename='0 or 
len(muffin_patches)',fig=my_fig,console_in=console,time_wait_between_lines=time_wait_between_lines); 
CodexAtLine(4,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    show_all(lineno=4,value=(0),valuename='0',fig=my_fig,console_in=console,time_wait_between_lines=time_wait_betwe
en_lines); CodexAtLine(4,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    show_all(lineno=4,value=(len(kid_patches) == 0 or len(muffin_patches) == 0),valuename='len(kid_patches) == 0 or
len(muffin_patches) == 0',fig=my_fig,console_in=console,time_wait_between_lines=time_wait_between_lines); 
CodexAtLine(4,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    if len(kid_patches) == 0 or len(muffin_patches) == 0:
        show_all(lineno=5,value=("Cannot determine fairness without kids or muffins in the 
image."),valuename='"Cannot determine fairness without kids or muffins in the 
image."',fig=my_fig,console_in=console,time_wait_between_lines=time_wait_between_lines); 
CodexAtLine(5,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
        return 'Cannot determine fairness without kids or muffins in the image.'
    num_kids = len(kid_patches)
    show_all(lineno=6,value=(num_kids),valuename='num_kids',fig=my_fig,console_in=console,time_wait_between_lines=t
ime_wait_between_lines); CodexAtLine(6,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    num_muffins = len(muffin_patches)
    show_all(lineno=7,value=(num_muffins),valuename='num_muffins',fig=my_fig,console_in=console,time_wait_between_l
ines=time_wait_between_lines); CodexAtLine(7,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    muffins_per_kid = num_muffins // num_kids
    show_all(lineno=8,value=(muffins_per_kid),valuename='muffins_per_kid',fig=my_fig,console_in=console,time_wait_b
etween_lines=time_wait_between_lines); CodexAtLine(8,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    show_all(lineno=9,value=(f'Each kid can have {muffins_per_kid} muffin(s) for it to be 
fair.'),valuename='f\'Each kid can have {muffins_per_kid} muffin(s) for it to be 
fair.\'',fig=my_fig,console_in=console,time_wait_between_lines=time_wait_between_lines); 
CodexAtLine(9,syntax=syntax,time_wait_between_lines=time_wait_between_lines)
    return f'Each kid can have {muffins_per_kid} muffin(s) for it to be fair.'''
exec(compile(code_line, 'Codex', 'exec'), globals())
print("Executing code 4.1")
result = execute_command(im, my_fig, time_wait_between_lines, syntax)  # The code is created in the exec()