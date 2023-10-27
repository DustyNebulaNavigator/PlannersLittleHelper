import { Link, useMatch, useResolvedPath } from "react-router-dom"
import './navbar.css'

export default function Navbar(){
    
    return (
        <div className="nav">
            <a href="#" className="site-title">PlannersLittleHelper</a>
            <ul>
                <CustomLink to='/'>Home</CustomLink>
                <CustomLink to='/cycletimes/'>SV1 cycles</CustomLink>
                <CustomLink to='/getPartDescription/'>Get by ID</CustomLink>
                <CustomLink to='/macinecyclestats/?machine_name=M0202&lookback_days=1&interval_minutes=30'>TEST</CustomLink>
            </ul>
        </div>
    )
}

function CustomLink({to, children, ...props}) {
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({path: resolvedPath.pathname})

    return (
        <li className={isActive ? 'active' : ''}>
            <Link to={to} {...props} >{children}</Link>
        </li>
    )
}