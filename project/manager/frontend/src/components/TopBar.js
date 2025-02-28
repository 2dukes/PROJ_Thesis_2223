import * as React from 'react';
import { Fragment, useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import ListItemIcon from '@mui/material/ListItemIcon';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import ExtensionIcon from '@mui/icons-material/Extension';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import { Link, useLocation } from 'react-router-dom';

const drawerWidth = 240;
const navItems = ['Available Scenarios', 'Solved Scenarios'];

const TopBar = () => {
  const [mobileOpen, setMobileOpen] = useState(false);

  const location = useLocation();
  const linkTo = ["/", "/solved"];

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const drawer = (
    <Box onClick={handleDrawerToggle} sx={{ textAlign: 'center' }}>
      <List>
        {navItems.map((text, index) => (
          <Link to={linkTo[index]} key={text} style={{ color: 'inherit', textDecoration: 'inherit' }}>
            <ListItem key={text} disablePadding style={{ backgroundColor: location.pathname === linkTo[index] ? 'lightgray' : 'white' }}>
              <ListItemButton>
                <ListItemIcon>
                  {index % 2 === 0 ? <ExtensionIcon /> : <CheckCircleIcon />}
                </ListItemIcon>
                <ListItemText primary={text} />
              </ListItemButton>
            </ListItem>
          </Link>
        ))}
      </List>
      <Divider />
    </Box>
  );

  const container = window.document.body;

  return (
    <Fragment>
      <AppBar component="nav" sx={{ backgroundColor: 'darkorange' }}>
        <Toolbar>

          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: 'none' } }}
          >
            <MenuIcon />
          </IconButton>

          <Typography
            variant="h6"
            noWrap
            component="div"
            href=""
            sx={{
              mr: 2,
              flexGrow: 1,
              fontFamily: 'monospace'
            }}
          >
            CR Manager
          </Typography>

          <Box sx={{ display: { xs: 'none', sm: 'block' } }}>
            {navItems.map((item, index) => (
              <Link to={linkTo[index]} key={item} style={{ color: 'inherit', textDecoration: 'inherit' }}>
                <Button key={item} style={{ color: 'white', backgroundColor: location.pathname === linkTo[index] ? 'black' : 'darkorange' }}>
                  {item}
                </Button>
              </Link>
            ))}
          </Box>
        </Toolbar>
      </AppBar>
      <Box component="nav">
        <Drawer
          container={container}
          variant="temporary"
          open={mobileOpen}
          onClose={handleDrawerToggle}
          ModalProps={{
            keepMounted: true, // Better open performance on mobile.
          }}
          sx={{
            display: { xs: 'block', sm: 'none' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
          }}
        >
          {drawer}
        </Drawer>
      </Box>
    </Fragment >
  );
};

export default TopBar;