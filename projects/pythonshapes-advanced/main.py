from colorama import Back

triangle = f"""
                              00
                             0{Back.WHITE}  {Back.RESET}0
                            1{Back.WHITE}    {Back.RESET}1
                           0{Back.WHITE}      {Back.RESET}0
                          1{Back.WHITE}        {Back.RESET}1
                         0{Back.WHITE}          {Back.RESET}0
                        1{Back.WHITE}            {Back.RESET}1
                       0{Back.WHITE}              {Back.RESET}0
                      1{Back.WHITE}                {Back.RESET}1
                     0{Back.WHITE}                  {Back.RESET}0
                    1{Back.WHITE}                    {Back.RESET}1
                   0{Back.WHITE}                      {Back.RESET}0
                  1{Back.WHITE}                        {Back.RESET}1
                 0{Back.WHITE}                          {Back.RESET}0
                1{Back.WHITE}                            {Back.RESET}1
                +0 1 0 1 0 1 0 1 0 1 0 1 0 1 +
"""
print(triangle)

circle = f"""
                       1 0 1 0 1 0 1
                   1 0{Back.WHITE}               {Back.RESET}0 1
                 0{Back.WHITE}                       {Back.RESET}0
                1{Back.WHITE}                         {Back.RESET}1
               0{Back.WHITE}                           {Back.RESET}0
               1{Back.WHITE}                           {Back.RESET}1
               0{Back.WHITE}                           {Back.RESET}0
                1{Back.WHITE}                         {Back.RESET}1
                 0{Back.WHITE}                       {Back.RESET}0
                   1{Back.WHITE}                  {Back.RESET}0 1
                     0 1 0 1 0 1 0  1
"""
print(circle)
