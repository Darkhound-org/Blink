# Copyright 2022 Darkhound-org

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from email.policy import default
from typing_extensions import Required
import click
import configparser
import pyshorteners
import pyperclip
import webbrowser
from quo import echo
from quo import print
import linsh_conf



@click.version_option('2022.08.20',prog_name='Linsh' )

@click.group(invoke_without_command=True, no_args_is_help=True)
@click.option('--license','-li',is_flag=True)
@click.option('--about','-a',is_flag=True)
@click.option('--github_repo','-ro',is_flag=True)
@click.option('--darkhound_org','-?',is_flag=True)
def cli(license,about,github_repo,darkhound_org):
    if license:

        print('''

Copyright 2022 Darkhound-org
SPDX-License-Identifier: Apache-2.0  
    
    ''')
    elif about:
        print('''
        
        Link shortner 

        ''')

    elif github_repo:
        print('''
        
        Opening link to Github repository in your default browser...

        https://github.com/Darkhound-org/Linsh 

        ''')    

    elif darkhound_org:
        
        print('\n\t\t\tWe '+'<red>Love</red>'+' CLI')
        
        print('''

        Darkhound-org develops applications [games too..] programmed in different languages [python,golang,lua..etc]

        Website: https://lantgz7548043.wixsite.com/darkhound-org
        Github: https://github.com/darkhound-org

        ''')    

    pass
       



@click.command()
@click.option('--url','-u',prompt=True)
@click.option('--open','-o', is_flag=True)
def tiny_url(url,open):
    try:

        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(url)
        
        print("Shortened URL: " + short_url)

        pyperclip.copy(short_url)
        print('Link copied to clip board..!!')

    except Exception:
         echo("!! Failed connecting to api !!", fg="red" , bold=True)
         
    
    if open:
        webbrowser.open(short_url)
    


@click.command()
@click.option('--url','-u',prompt=True)
@click.option('--open','-o', is_flag=True)
@click.option('--total_clicks','-tc',is_flag=True)
def bitly(url,open,total_clicks):
    try:
        config = linsh_conf.read_conf()
        api_bx = config['Bitly']['api-key']
        type_bitly = pyshorteners.Shortener(api_key=api_bx)
        bshort_url = type_bitly.bitly.short(url)
 
        print("Shortened URL: " + bshort_url)
        pyperclip.copy(bshort_url)
        print('Link copied to clip board..!!')
    except Exception:

            echo("!! Failed connecting to api !!", fg="red" , bold=True)

    
    if open:
        webbrowser.open(bshort_url)
    elif total_clicks:
        tck = type_bitly.bitly.total_clicks(bshort_url)  
        print("Total clicks: " + tck)

@click.command()    
@click.option('--url','-u',prompt=True)
@click.option('--open','-o', is_flag=True) 
def chilp(url,open):
    try:
        type_chilp = pyshorteners.Shortener()
        short_ch_url = type_chilp.chilpit.short(url)
        print("Shortened URL: " + short_ch_url)
        pyperclip.copy(short_ch_url)
        print('Link copied to clip board..!!')

    except Exception:
             echo("!! Failed connecting to api !!", fg="red" , bold=True)


    if open:
        webbrowser.open(short_ch_url)  

@click.command()
@click.option('--url','-u',prompt=True)
@click.option('--open','-o', is_flag=True) 
def cuttly(url,open):
    try:
        config = linsh_conf.read_conf()
        api_cx = config['Cuttly']['api-key']
        type_cuttly = pyshorteners.Shortener(api_key=api_cx)
        cushort_url = type_cuttly.cuttly.short(url)
 
        print("Shortened URL: " + cushort_url)
        pyperclip.copy(cushort_url)
        print('Link copied to clip board..!!')
    except Exception:
             echo("!! Failed connecting to api !!", fg="red" , bold=True)

    if open:
        webbrowser.open(cushort_url)



cli.add_command(tiny_url)    
cli.add_command(bitly)
cli.add_command(chilp)
cli.add_command(cuttly)


if __name__=="__main__":
    cli()            





