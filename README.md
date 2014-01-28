finddomain
======

This little python script is intended to find the shorter domain names
that still are unregistered.

## Requirements

  * whois (not python whois, the stand-alone whois)

## Usage

    finddomain [OPTIONS]

### Available options
  * -c --length _LENGTH_  
     The length of your desired domain name  
     Default: 4
  * -t --top-level-domain _TLD_  
    The TLD you want to search in.  
    If not specified it will try most of the top level domains that exists  
    at the time of writing.
  * -l --letters _LETTERS_  
    The letters you want your domain to contain.  
    Default: [a-zA-Z0-9-]
  * -s --sleep _SECONDS_  
    Some whois servers may temporarily ban you when doing many queries in short notice.  
    The argument can be written as a fractal.  
    Default: 1
      
### Example
    finddomain -c 3 -t se -l abc  

or

    finddomain --length=3 --top-level-domain=se --letters=abc

Will output:  

    abc.se is unavailable.
    acb.se is unavailable.
    bac.se is unavailable.
    bca.se is unavailable.
    cab.se is unavailable.
    cba.se is unavailable.

## Licensing

All code is licensed under the terms of the 3-clause BSD-License:

    Copyright (c) 2014, jocke-l
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
          notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution.
        * The names of the authors must not be used to endorse or promote
          products derived from this software without specific prior written
          permission.
      
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS AS IS AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY
    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR  CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
